#!/usr/bin/env python3
"""Optional public-data API fetcher for extra Busan tourism-demand context.
Requires an authorized data.go.kr service key in a LOCAL environment variable.
This cannot measure causal outcomes of our recommender or human relevance.
Never commit downloaded private data or credentials.
"""
import argparse
import json
import os
import re
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import urlencode,unquote
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError

SERVICES={
 "food_spending_demand":("https://apis.data.go.kr/B551011/AreaTarResDemService/areaTarSvcDemList","tarSvcDemIxCd","1106"),
 "shopping_spending_demand":("https://apis.data.go.kr/B551011/AreaTarResDemService/areaTarSvcDemList","tarSvcDemIxCd","1105"),
 "accommodation_spending_demand":("https://apis.data.go.kr/B551011/AreaTarResDemService/areaTarSvcDemList","tarSvcDemIxCd","1107"),
 "spending_per_visit_intensity":("https://apis.data.go.kr/B551011/AreaTarDemDsService/areaTarExpDsList","tarExpDsIxCd","2203"),
}

def run(month,district,indicator,output_dir,dry_run=False):
    if not re.fullmatch(r"20\d{4}",month) or not 1<=int(month[-2:])<=12:
        raise ValueError("Invalid YYYYMM")
    if not re.fullmatch(r"26\d{3}",district):
        raise ValueError("Expected five-digit Busan signgu code; verify against service guide")
    endpoint,param_name,metric_code=SERVICES[indicator]
    params={"numOfRows":100,"pageNo":1,"MobileOS":"ETC","MobileApp":"BusanResearch",
            "baseYm":month,"areaCd":"26","signguCd":district,
            param_name:metric_code,"_type":"json"}
    if dry_run:
        return {"status":"DRY_RUN_NO_NETWORK","indicator":indicator,
                "parameters_without_secret":params}
    key=os.environ.get("KTO_DATA_GO_KR_SERVICE_KEY")
    if not key: raise RuntimeError("Missing authorized API key in local environment")
    url=endpoint+"?"+urlencode({**params,"serviceKey":unquote(key)})
    try:
        with urlopen(Request(url,headers={"User-Agent":"BusanResearch/1.0"}),timeout=20) as result:
            raw=result.read(3000000)
    except (HTTPError,URLError,TimeoutError):
        # NEVER echo HTTP exceptions: they can contain secret-bearing URLs.
        raise RuntimeError("API failed; check approval, district codes and service access") from None
    try: data=json.loads(raw)
    except Exception: raise RuntimeError("API response was not valid JSON") from None
    if not isinstance(data,dict):raise RuntimeError("Unexpected response")
    header=(data.get("response") or {}).get("header") or data.get("header") or {}
    if str(header.get("resultCode","00")) not in {"00","0000","0","OK"}:
        raise RuntimeError("Provider reports a non-success result; inspect key/codes privately")
    folder=Path(output_dir).expanduser()
    folder.mkdir(parents=True,exist_ok=True)
    filepath=folder/f"{month}_{district}_{indicator}.json"
    if filepath.exists():raise FileExistsError("Destination already exists; protect old evidence")
    filepath.write_text(json.dumps({
      "timestamp_utc":datetime.now(timezone.utc).isoformat(),
      "source":endpoint,"parameters_without_secret":params,
      "api_response":data,
      "research_warning":"Demand statistics are not effects of experimental recommendations"},
      ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return {"status":"DOWNLOADED_UNAUDITED","path":str(filepath),
            "warning":"Inspect source definitions and permissions before analysis"}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--month",required=True)
    p.add_argument("--district",required=True)
    p.add_argument("--indicator",choices=SERVICES,default="food_spending_demand")
    p.add_argument("--output-dir",default=str(Path.home()/"busan_research_private"/"kto_api"))
    p.add_argument("--dry-run",action="store_true")
    args=p.parse_args()
    try: result=run(args.month,args.district,args.indicator,args.output_dir,args.dry_run)
    except (ValueError,RuntimeError,FileExistsError) as e:p.error(str(e))
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__":main()
