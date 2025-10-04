from psdi.util import MXApplicationException;
from java.io import FileOutputStream;
from java.io import FileInputStream;
from java.nio.file import Paths;
from java.nio.file import Files;
from java.util.zip import ZipOutputStream;
from java.util.zip import ZipEntry;
from java.io import File;

if launchPoint=='<ActionName>':
    session=service.webclientsession()
    docTable=session.getDataBean("<dialog_id>")
    docVector=docTable.getSelection()
    
    filePaths=[]
    for doc in docVector:
        file=doc.getString("URLNAME")
        filePaths.append(file)
    
    downLoadPath="C:\\Users\\Public\\Downloads\\";
    fullPath=downLoadPath+"<FileName>.zip";
    fos = FileOutputStream(fullPath);
    zipOut = ZipOutputStream(fos);
  
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