# Official sources, provenance and reuse review

## Foreign tourist activity and spending

**Provider:** Korea Tourism Data Lab (Korea Tourism Organization).

- Main portal: https://datalab.visitkorea.or.kr/datalab/portal/main/getMainForm.do
- Regional tourism data: https://datalab.visitkorea.or.kr/datalab/portal/loc/getAreaFocTourBeta.do
- Visitor indicator: 지역별 관광 현황 → 외국인 방문자수.
- Spending indicator: 지역 관광소비 → 외국인 신용카드 관광소비 추이.

**Coverage of the local research export:** 16 Busan districts × 2022–2025 monthly intervals, assembled from 64 visitor and 64 foreign-card-consumption district-year downloads.

**Interpretation:** Visitor activity is mobility-derived estimation, not a count of unique persons. Foreign card consumption is only part of tourism spending and uses millions of Korean won in the processed panel.

## Official attractions

**Provider:** Busan Metropolitan City, Busan Attractions Information Service (부산명소정보 서비스).

- Korean Public Data Portal record: https://www.data.go.kr/data/15063481/openapi.do
- Busan portal: https://data.busan.go.kr/bdip/opendata/detail.do?publicdatapk=15063481
- Data service: https://apis.data.go.kr/6260000/AttractionService

The local research dataset includes 207 attraction records. The API may have its own reuse terms, distinct from the Korea Tourism Data Lab terms.

## Current legal/attribution status

The Data Lab dataset redistribution terms are still unconfirmed; the attraction catalog permission field was separately checked below. Before placing the entire 768-row panel, the combined JSON database, or raw ZIP downloads in this **public** repository:

1. Read and document each provider's current license, terms of use, attribution requirements and redistribution restrictions.
2. Check any API-specific limits or terms of use; verify whether public republishing of downloaded tables is allowed.
3. Record exact download/filter parameters and dates and retain original checksums where available.
4. Exclude all API tokens, login cookies, private access keys, authentication headers and personal details.
5. If the datasets cannot be publicly redistributed, keep them in private local or approved institutional storage and provide reproduction instructions rather than copies.

Derived summary metrics and authored methodological descriptions are being organized separately in this change. This is not legal advice or an assertion of open licensing.


## Provider-page checks, 2026-11-13

- The [official attraction catalog](https://www.data.go.kr/data/15063481/openapi.do)
  identifies Busan Metropolitan City as provider, catalog ID 15063481, and
  displays “이용허락범위 제한 없음” (no restriction in the permission-scope field).
  Its endpoint and record-field descriptions match the existing snapshots.
  This is not a verified blanket license for every linked photograph or website.
  No photographs have been downloaded or republished in this update.
- The [Data Lab portal](https://datalab.visitkorea.or.kr/datalab/portal/main/getMainForm.do)
  lists mobility and card-consumption products and states that collection must
  use its officially provided download methods. Its terms link redirected to
  the homepage during this check, so dataset-specific redistribution permission
  could not be established. Do not newly publish the panel or combined JSON.
- [Public Data Portal policy](https://www.data.go.kr/ugs/selectPortalPolicyView.do)
  and [Korea Tourism Organization copyright policy](https://knto.or.kr/helpdeskCopyrightguide)
  are reference pages, not substitutes for the applicable data-product terms.

The 768-row coverage and 128-download history above are claims in the prior
archive documentation, not verified against original downloads here. Exact
acquisition dates and export settings remain unknown. Existing Data Lab CSVs
were already on main and remain unchanged; this update does not newly certify
or expand their redistribution rights.
