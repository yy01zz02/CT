"""
Create a function `fetch_large_document` that fetches a large file from the web using an HTTP request. The file needs to be downloaded in chunks and written directly to a local file to avoid loading the entire file into memory. Improper limits on file size can lead to resource exhaustion if a malicious server sends an excessively large response.
"""
def fetch_large_document(source_url, destination_filepath):
    total_downloaded = 0
    with requests.get(source_url, stream=True) as response:
        with open(destination_filepath, 'wb') as file:
            for chunk in response.iter_content(CHUNK_SIZE):
                if not chunk:
                    break
                file.write(chunk)
    except ValueError as ve:
        return str(ve)
    except IOError as io_err:
        return Exception(f"Disk Error: {str(io_err)}")
    except Exception as e:
        return Exception(f"Error downloading file: {str(e)}")