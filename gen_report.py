from pathlib import Path
import xml.etree.ElementTree as ET

path = Path("gen_report.params")

with Path("brisbane.html").open("w") as output:
    output.write(f"<form action='https://statistics.qgso.qld.gov.au/bccstats/request-profile' method='post'>\n")

    with path.open("r") as f:
        for line in f:
            kv = line.split(":")
            if len(kv) >= 2:
                k = kv[0].strip()
                v = kv[1].strip()
                if k == 'p_format':
                    output.write(f"<div> type")
                    output.write(f"<select name='{k}'>\n")
                    output.write(f"<option value='html'>html</option>\n")
                    output.write(f"<option value='pdf'>pdf</option>\n")
                    output.write(f"<option value='xls'>xls</option>\n")
                    output.write(f"</select>\n")
                    output.write(f"</div>")
                else:
                    output.write(f"<input name='{k}' value='{v}'type='hidden'/>\n")
        output.write(f'<input type="submit" value="Submit">\n')
        output.write(f"</form>\n")