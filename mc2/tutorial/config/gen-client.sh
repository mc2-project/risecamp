#!/bin/sh

# Set client's name
if [ "$#" -ne 1 ]; then
    echo "Usage: ./gen-client.sh <username>"
    exit 1
fi
USERNAME=$1

# Generate keypair for client
echo "Generating keypair"
openssl genrsa -out config/${USERNAME}.pem -3 3072

# Generate a certificate signing request
echo "Generating CSR"
openssl req -new -key config/${USERNAME}.pem -out config/${USERNAME}.csr -subj "/CN=${USERNAME}"

# Generate a certificate for the client signed by the root CA
echo "Signing CSR"
openssl x509 -req -in config/${USERNAME}.csr -days 3650 -CA config/root.crt -CAkey config/root.pem -CAcreateserial -out config/${USERNAME}.crt

rm config/${USERNAME}.csr
rm config/*.srl
