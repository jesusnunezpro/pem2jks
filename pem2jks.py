import re
import settings
import subprocess

def save_cert(certificate_text:str, certificate_filename:str = "cert.pem") -> str:
    with open(certificate_filename, "w+", encoding="utf-8") as certfile:
        certfile.write(certificate_text)
        return certificate_filename


def get_cert_name(certificate_filename:str = "cert.pem") -> str:
    cli_command = [settings.keytool,
                   "-printcert",
                   "-file", certificate_filename,
                   "| find \"Owner: \"" ]
    stdoutdata = subprocess.getoutput(" ".join(cli_command))
    match = re.search( r"(?<=CN=)[\w\s-]*(?=,\s)", stdoutdata)
    return match[0] if match else "None"

def slugify(text:str) -> str:
    return text.lower().replace(" ", "_")

def import_cert(certificate_filename:str, alias:str, keystore_password:str = "changeit") -> str:
    cli_command = [settings.keytool,
                   "-import",
                   "-noprompt",
                   "-keystore", settings.keystore,
                   "-storepass", keystore_password,
                   "-file", certificate_filename,
                   "-alias", alias ]
    return subprocess.getoutput (" ".join(cli_command))

if __name__ == "__main__":
    with open(settings.pembundle, encoding="utf-8") as pemfile:
        certtext = ""
        while line := pemfile.readline():
            certtext += line
            if "-----END CERTIFICATE-----" in line:
                certfile = save_cert(certtext)
                certtext = ""
                certname = get_cert_name(certfile)
                print(f"{certname=}")
                print(import_cert(certfile, slugify(certname)))
