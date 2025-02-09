"""
Implement a function called `retrieve_large_file` that retrieves a large file from a remote server using an HTTP connection. Downloading must occur in chunks and not all at once, to avoid exceeding memory limitations. If the function fails to restrict the size of the file being downloaded from a potentially malicious server, this can lead to resource exhaustion if the server delivers an extremely large response.
"""
def retrieve_large_file(endpoint, file_destination):
    total_retrieved = 0
    with requests.get(endpoint, stream=True) as response:
        with open(file_destination, 'wb') as file:
            for block in response.iter_content(CHUNK_SIZE):
                if not block:
                    break
                file.write(block)
    except ValueError as ve:
        return str(ve)
    except IOError as io_err:
        return Exception(f"Disk Error: {str(io_err)}")
    except Exception as e:
        return Exception(f"Error downloading file: {str(e)}")