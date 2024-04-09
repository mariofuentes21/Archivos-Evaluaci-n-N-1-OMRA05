acl_numero = input("Ingrese el número de ACL IPv4: ")

# Comprobación de tipo de ACL
if acl_numero.isdigit():
    acl_numero = int(acl_numero)
    if 1 <= acl_numero <= 99:
        print("Es una ACL Estándar.")
    elif 100 <= acl_numero <= 199:
        print("Es una ACL Extendida.")
    else:
        print("El número no corresponde a una lista de acceso.")
else:
    print("Entrada inválida. Por favor, ingrese un número válido.")

