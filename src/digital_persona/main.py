import win32com.client

fingerprint_reader = win32com.client.Dispatch("DPFPDev.DPFDevCtl")

fingerprint_reader.Init()

print("Conectando al lector de huellas....")

if fingerprint_reader.ReaderCount > 0:
    print("Lector encontrado: ", fingerprint_reader.ReaderName)
else:
    print("No se encontro ningun lector")

    
fingerprint_reader.Close()