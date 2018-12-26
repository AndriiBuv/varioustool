
import requests, os, os.path


url = 'http://www.planetpublish.com/wp-content/uploads/2011/11/The_Jungle_Book_T.pdf'
local_filename = 'Test.pdf'

def download_file(url, fname):

    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(fname, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    f.close()
    print ('File %s is loaded and has size of %s' % (fname, os.path.getsize(os.path.abspath(fname))))
                #f.flush() commented by recommendation from J.F.Sebastian
    return f

download_file(url, local_filename)

