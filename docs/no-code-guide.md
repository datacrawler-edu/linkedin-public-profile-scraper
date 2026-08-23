# Run LinkedIn Public Profile Scraper without code

You can scrape public LinkedIn profile URLs from Apify's web interface. You do
not need Python, an API token, a LinkedIn account, a LinkedIn login or cookies.

## Step-by-step

1. Open [LinkedIn Public Profile Scraper on Apify](https://apify.com/datascraperes/linkedin-public-profile-scraper?fpr=edudata).
2. Select the **Input** tab.
3. Add one or more URLs in **LinkedIn profile URLs**. Use URLs such as `https://www.linkedin.com/in/public-identifier/`.
4. Click **Start** and wait for the run to finish.
5. Open the **Dataset** tab.
6. Check `success`, `status`, `profile.fullName` and `dataQuality`.
7. Export the Dataset as JSON, CSV or Excel.

## First test

The checked-in [`data/sample-input.json`](../data/sample-input.json) shows the
required `profileUrls` array and includes a deliberately invalid company URL.
Replace the example URL with a real public profile URL when testing the Actor.

## What the result means

- `success` with `status: "success"` means public profile data was extracted.
- `invalid_url` means the input is not a `/in/` profile URL.
- `not_found` means no public profile was found at that URL.
- `blocked`, `rate_limited` or `network_error` can be retried later.
- `login_required` means that particular page was not available in LinkedIn's
  public guest view. It does not mean that you should provide credentials.

## Use the monthly free usage credit

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the
Apify Store or your own Actors, and no credit card is required to start. Test a
small number of public URLs first. The credit is not unlimited, and unused
credit expires at the end of the billing cycle.

See the [current Apify pricing](https://apify.com/pricing?fpr=edudata) for the
current terms.
