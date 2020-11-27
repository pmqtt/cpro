from watchdog.events import FileSystemEventHandler
import os
class HandleFilesystemEvent(FileSystemEventHandler):
    def on_created(self,event):
        path,file= os.path.split(event.src_path)
        if event.src_path.lower().startswith(('./src/','./header')):
            if file.lower().endswith(('cpp','hpp','c','h','cxx','hxx')):
                f = open('CMAKE_FILES.txt','r+b')
                f.seek(-1,2) #whence 2 means relative to the end of file
                f.write(b'\n\t')
                f.write(bytes(event.src_path,'utf-8'))
                f.write(b')')
                f.flush()
                f.close()
                os.system('cmake .')



    #def on_deleted(self,event):

    #def on_modified(self,event):

    #def on_moved(self,event):
