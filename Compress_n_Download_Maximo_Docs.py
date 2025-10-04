from psdi.util import MXApplicationException;
from java.io import FileOutputStream;
from java.io import FileInputStream;
from java.nio.file import Paths;
from java.nio.file import Files;
from java.util.zip import ZipOutputStream;
from java.util.zip import ZipEntry;
from java.io import File;

if launchPoint=='<ActionName>':
    #Get the dialog bean
    session=service.webclientsession()
    docTable=session.getDataBean("<dialog_id>")
    
    #Get the selection of files/attachments from dialog
    docVector=docTable.getSelection()
    
    #Add the file paths/doclink URLs to an array
    filePaths=[]
    for doc in docVector:
        file=doc.getString("URLNAME")
        filePaths.append(file)
    
    #Set the download folder, filenames
    downLoadPath="C:\\Users\\Public\\Downloads\\";
    fullPath=downLoadPath+"<FileName>.zip";
    
    #Initiate the file, zip-file output stream
    fos = FileOutputStream(fullPath);
    zipOut = ZipOutputStream(fos);
    
    #Read each file and write into zip file.
    try:
        for filePath in filePaths:
            fileToZip = File(filePath);
            fis = FileInputStream(fileToZip);
            zipEntry = ZipEntry(fileToZip.getName());
            zipOut.putNextEntry(zipEntry);
            bytes = Files.readAllBytes(Paths.get(filePath));
            zipOut.write(bytes, 0, len(bytes));
            fis.close();
        zipOut.close();
        fos.close();
        print ("Compressed the Files to " +str(fullPath));        
																   
    except MXApplicationException as me:
        print ("Maximo Error : " + str(e));
    except Exception as e :
        print ("Error : " + str(e));
