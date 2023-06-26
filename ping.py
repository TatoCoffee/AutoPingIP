import subprocess

# Lista de archivos de texto con las direcciones IP
archivos_ips = ["textplane\ping1.txt", "textplane\ping2.txt", "textplane\ping3.txt"]

# Función para realizar el ping a una IP específica
def hacer_ping(ip):
    try:
        # Ejecutar el comando de ping
        output = subprocess.check_output(["ping", "-n", "4", ip], stderr=subprocess.STDOUT, universal_newlines=True)
        print(f"Ping exitoso a {ip}")
        print(output)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Ping fallido a {ip}")
        print(e.output)
        return False

# Mostrar el menú
while True:
    print("Seleccione una opción:")
    print("1. Seleccionar un archivo de texto y hacer ping a una IP específica")
    print("2. Seleccionar un archivo de texto y hacer ping a todas las IPs")
    print("0. Salir")

    seleccion = input("Ingrese el número correspondiente: ")
    seleccion = int(seleccion)

    if seleccion == 0:
        break

    if seleccion < 1 or seleccion > 2:
        print("Selección inválida. Intente nuevamente.")
        continue

    if seleccion == 1:
        print("Seleccione un archivo de texto para realizar el ping:")
        for i, archivo_ips in enumerate(archivos_ips):
            print(f"{i+1}. {archivo_ips}")

        seleccion_archivo = input("Ingrese el número correspondiente (0 para cancelar): ")
        seleccion_archivo = int(seleccion_archivo)

        if seleccion_archivo == 0:
            continue

        if seleccion_archivo < 1 or seleccion_archivo > len(archivos_ips):
            print("Selección inválida. Intente nuevamente.")
            continue

        archivo_seleccionado = archivos_ips[seleccion_archivo - 1]

        # Leer el archivo de texto y obtener las IPs
        with open(archivo_seleccionado, "r") as file:
            ips = file.readlines()
            ips = [ip.strip() for ip in ips]

        # Mostrar las IPs disponibles para elegir
        print(f"IPs disponibles en el archivo '{archivo_seleccionado}':")
        for i, ip in enumerate(ips):
            print(f"{i+1}. {ip}")

        seleccion_ip = input("Seleccione una IP (ingrese el número correspondiente): ")
        seleccion_ip = int(seleccion_ip)

        if seleccion_ip < 1 or seleccion_ip > len(ips):
            print("Selección inválida. Intente nuevamente.")
            continue

        ip_seleccionada = ips[seleccion_ip - 1]

        print(f"Haciendo ping a {ip_seleccionada}...")
        hacer_ping(ip_seleccionada)
        print()

        # Resumen de IPs fallidas
        exitosos = 0
        fracasos = 0
        ips_fallidas = []

        if hacer_ping(ip_seleccionada):
            exitosos += 1
        else:
            fracasos += 1
            ips_fallidas.append(ip_seleccionada)

        print(f"Resumen:")
        print(f"Operaciones exitosas: {exitosos}")
        print(f"Operaciones fallidas: {fracasos}")
        print("IPs Fallidas:")
        for ip in ips_fallidas:
            print(ip)

    elif seleccion == 2:
        print("Seleccione un archivo de texto para realizar el ping:")
        for i, archivo_ips in enumerate(archivos_ips):
            print(f"{i+1}. {archivo_ips}")

        seleccion_archivo = input("Ingrese el número correspondiente (0 para cancelar): ")
        seleccion_archivo = int(seleccion_archivo)

        if seleccion_archivo == 0:
            continue

        if seleccion_archivo < 1 or seleccion_archivo > len(archivos_ips):
            print("Selección inválida. Intente nuevamente.")
            continue

        archivo_seleccionado = archivos_ips[seleccion_archivo - 1]

        # Leer el archivo de texto y obtener las IPs
        with open(archivo_seleccionado, "r") as file:
            ips = file.readlines()
            ips = [ip.strip() for ip in ips]

        print(f"Haciendo ping a todas las IPs en el archivo '{archivo_seleccionado}'...")
        
        # Resumen de IPs fallidas
        exitosos = 0
        fracasos = 0
        ips_fallidas = []

        for ip in ips:
            print(f"Ping a {ip}...")
            if hacer_ping(ip):
                exitosos += 1
            else:
                fracasos += 1
                ips_fallidas.append(ip)
            print()

        print(f"Resumen:")
        print(f"Operaciones exitosas: {exitosos}")
        print(f"Operaciones fallidas: {fracasos}")
        print("IPs Fallidas:")
        for ip in ips_fallidas:
            print(ip)

print("Saliendo del programa.")