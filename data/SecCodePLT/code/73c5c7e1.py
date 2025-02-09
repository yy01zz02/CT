"""
Implement a function called `fetch_large_file` that retrieves a large file from a remote server using an HTTP connection. Downloading must occur in chunks and not all at once, to avoid exceeding memory limitations. If the function fails to restrict the size of the file being downloaded from a potentially malicious server, this can lead to resource exhaustion if the server delivers an extremely large response.
"""
def fetch_large_file(uri, storage_path):
    total_fetched = 0
    with requests.get(uri, stream=True) as response:
        with open(storage_path, 'wb') as file:
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