import subprocess

def ssh_in_new_mac_terminal(hosts):
    for host in hosts:
        command = f"cx {host}"
        subprocess.Popen([
            "osascript", "-e",
            f'tell application "Terminal" to do script "{command}"'
        ])
       

# Example usage
hosts = [
"st51p01if-quln06110101.st.if.apple.com",
"st53p01if-quln02111302.st.if.apple.com",
"st53p01if-quln03101702.st.if.apple.com",
"st53p01if-quln08112101.st.if.apple.com",
"st54p01if-quln03101301.st.if.apple.com",
"st56p01if-quln11110301.st.if.apple.com",
"st56p01if-quln11161102.st.if.apple.com",
"st56p01if-quln12160902.st.if.apple.com",
"st57p01if-quln03012101.st.if.apple.com",
"st57p01if-quln03012301.st.if.apple.com",
"st57p01if-quln03100302.st.if.apple.com",
"st57p01if-quln03101102.st.if.apple.com",
"st57p01if-quln03200102.st.if.apple.com",
"st57p01if-quln03200902.st.if.apple.com",
"st57p01if-quln04080501.st.if.apple.com",
"st57p01if-quln04081502.st.if.apple.com",
"st57p01if-quln05010301.st.if.apple.com",
"st57p01if-quln05010302.st.if.apple.com",
"st57p01if-quln05011102.st.if.apple.com",
"st57p01if-quln05201101.st.if.apple.com",
"st57p01if-quln15110102.st.if.apple.com",
"st57p01if-quln15120102.st.if.apple.com",
"st57p01if-quln15141302.st.if.apple.com",
"st57p01if-quln15162102.st.if.apple.com",
"st58p01if-quln10201102.st.if.apple.com",
"st58p01if-quln11201301.st.if.apple.com",
]
ssh_in_new_mac_terminal(hosts)
