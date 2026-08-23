# cURL request

Set `APIFY_API_TOKEN` in your shell and send the same `profileUrls` payload
used by the web interface. The synchronous endpoint waits for the run to
finish and returns the default Dataset items.

```bash
curl --request POST \
  "https://api.apify.com/v2/acts/datascraperes~linkedin-public-profile-scraper/run-sync-get-dataset-items?token=$APIFY_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data @data/sample-input.json
```

For a PowerShell request, use:

```powershell
$headers = @{ Authorization = "Bearer $env:APIFY_API_TOKEN" }
Invoke-RestMethod `
  -Method Post `
  -Uri "https://api.apify.com/v2/acts/datascraperes~linkedin-public-profile-scraper/run-sync-get-dataset-items" `
  -Headers $headers `
  -ContentType "application/json" `
  -Body (Get-Content .\data\sample-input.json -Raw)
```

Use a real public LinkedIn profile URL before expecting a successful profile
item. The checked-in sample is sanitized and intentionally contains an invalid
company URL to demonstrate the auditable `invalid_url` status.
