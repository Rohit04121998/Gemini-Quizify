import sys
import os
import streamlit as st

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir)
# sys.path.insert(1, "/path/to/tasks")  # replace with your own path if different
from task_3.task_3 import DocumentProcessor
from task_4.task_4 import EmbeddingClient


# Import Task libraries
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()
PROJECT_ID = os.environ["PROJECT_ID"]


class ChromaCollectionCreator:
    def __init__(self, processor, embed_model):
        """
        Initializes the ChromaCollectionCreator with a DocumentProcessor instance and embeddings configuration.
        :param processor: An instance of DocumentProcessor that has processed documents.
        :param embeddings_config: An embedding client for embedding documents.
        """
        self.processor = processor  # This will hold the DocumentProcessor from Task 3
        self.embed_model = embed_model  # This will hold the EmbeddingClient from Task 4
        self.db = None  # This will hold the Chroma collection

    def create_chroma_collection(self):
        """
        Task: Create a Chroma collection from the documents processed by the DocumentProcessor instance.

        Steps:
        1. Check if any documents have been processed by the DocumentProcessor instance. If not, display an error message using streamlit's error widget.

        2. Split the processed documents into text chunks suitable for embedding and indexing. Use the CharacterTextSplitter from Langchain to achieve this. You'll need to define a separator, chunk size, and chunk overlap.
        https://python.langchain.com/docs/modules/data_connection/document_transformers/

        3. Create a Chroma collection in memory with the text chunks obtained from step 2 and the embeddings model initialized in the class. Use the Chroma.from_documents method for this purpose.
        https://python.langchain.com/docs/integrations/vectorstores/chroma#use-openai-embeddings
        https://docs.trychroma.com/getting-started

        Instructions:
        - Begin by verifying that there are processed pages available. If not, inform the user that no documents are found.

        - If documents are available, proceed to split these documents into smaller text chunks. This operation prepares the documents for embedding and indexing. Look into using the CharacterTextSplitter with appropriate parameters (e.g., separator, chunk_size, chunk_overlap).

        - Next, with the prepared texts, create a new Chroma collection. This step involves using the embeddings model (self.embed_model) along with the texts to initialize the collection.

        - Finally, provide feedback to the user regarding the success or failure of the Chroma collection creation.

        Note: Ensure to replace placeholders like [Your code here] with actual implementation code as per the instructions above.
        """

        # Step 1: Check for processed documents
        if len(self.processor.pages) == 0:
            st.error("No documents found!", icon="🚨")
            return

        # Step 2: Split documents into text chunks
        # Use a TextSplitter from Langchain to split the documents into smaller text chunks
        # https://python.langchain.com/docs/modules/data_connection/document_transformers/character_text_splitter
        text_splitter = CharacterTextSplitter(
            separator=".", chunk_size=1000, chunk_overlap=100
        )

        # Split the processed documents into text chunks
        text_chunks = []

        for document in self.processor.pages:
            # Extract text content from the document
            text = document.page_content
            chunks = text_splitter.split_text(text)
            text_chunks.extend(chunks)

        st.write(
            f"Split {len(self.processor.pages)} document(s) into {len(text_chunks)} text chunks"
        )

        # Step 3: Create the Chroma Collection
        # https://docs.trychroma.com/
        # Create a Chroma in-memory client using the text chunks and the embeddings model
        # Initialize a Chroma collection
        chroma_collection = Chroma()

        # Iterate through each text chunk
        for chunk in text_chunks:
            # Get vector embedding for the text chunk
            embedding = embed_client.embed_query(chunk)

            # Add the text chunk and its embedding to the Chroma collection
            chroma_collection.add_document(chunk, embedding)

        # # Assign the Chroma collection to the class attribute
        self.db = chroma_collection

        # Provide feedback to the user regarding the success of the Chroma collection creation
        st.success("Chroma Collection created successfully!")
        # return chroma_collection

    def query_chroma_collection(self, query) -> Document:
        """
        Queries the created Chroma collection for documents similar to the query.
        :param query: The query string to search for in the Chroma collection.

        Returns the first matching document from the collection with similarity score.
        """
        if self.db:
            docs = self.db.similarity_search_with_relevance_scores(query)
            if docs:
                return docs[0]
            else:
                st.error("No matching documents found!", icon="🚨")
        else:
            st.error("Chroma Collection has not been created!", icon="🚨")


if __name__ == "__main__":
    processor = DocumentProcessor()  # Initialize from Task 3
    processor.ingest_documents()

    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": PROJECT_ID,
        "location": "us-central1",
    }

    embed_client = EmbeddingClient(**embed_config)  # Initialize from Task 4

    chroma_creator = ChromaCollectionCreator(processor, embed_client)

    with st.form("Load Data to Chroma"):
        st.write("Select PDFs for Ingestion, then click Submit")

        submitted = st.form_submit_button("Submit")
        if submitted:
            chroma_creator.create_chroma_collection()
