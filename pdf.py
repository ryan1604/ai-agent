import os
from llama_index import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers import PDFReader

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print(f'building index {index_name}')
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index

canada_pdf_path = os.path.join('data', 'Canada.pdf')
canada_pdf = PDFReader().load_data(file=canada_pdf_path)
canada_index = get_index(canada_pdf, 'canada')
canada_engine = canada_index.as_query_engine()

singapore_pdf_path = os.path.join('data', 'Singapore.pdf')
singapore_pdf = PDFReader().load_data(file=singapore_pdf_path)
singapore_index = get_index(singapore_pdf, 'singapore')
singapore_engine = singapore_index.as_query_engine()