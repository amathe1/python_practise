import re


text = """
The HTTPS service monitors all of the scan details of the HTTP service and the validity and 
expiry date of an SSL certificate on a device.

You can monitor the scan details for the SSL certificates only if the certificates have been 
signed by a CA that has been uploaded in N-able N-central or is listed in the default CA 
certificate file provided by N-able N-central.  For more information on uploading a certificate, see Uploading a certificate.

The HTTPS service also includes WTSS functionality that monitors the specific content on a 
web site over a secure web connection by searching for a matching regular expression. 
For example, you can monitor the availability of specific content on an e-commerce site 
that uses a database driven architecture. The results from monitoring are displayed on 
the status dashboard under the HTTP service. If specified, the results can also be provided 
in any notifications triggered by the service.

"""

"""
\S not space = [^\s]
\W not alphanumeric = [^\w]
\D not a digit = [^\d]

"""

notspace = set(re.findall("\S", text))
print(notspace)

print()

notalpha = set(re.findall("\W", text))
print(notalpha)
