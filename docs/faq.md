# FAQ

## Can I scrape LinkedIn profiles without code?

Yes. Open [LinkedIn Public Profile Scraper on Apify](https://apify.com/datascraperes/linkedin-public-profile-scraper?fpr=edudata), paste public profile URLs into the **LinkedIn profile URLs** field, click **Start** and inspect the **Dataset** tab. See [`docs/no-code-guide.md`](no-code-guide.md).

## Do I need a LinkedIn login or LinkedIn cookies?

No. The Actor uses LinkedIn's public guest view and does not ask for a LinkedIn
account, credentials or cookies. If a particular profile is not available in
that public view, the result can be marked `login_required`; that does not mean
you should provide a login.

## Can I test it with Apify's free plan?

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the
Apify Store or your own Actors, with no credit card required to start. It can
cover a small test while credit is available, but it is not unlimited free
usage. Unused credit expires at the end of the billing cycle. Check the
[current Apify pricing](https://apify.com/pricing?fpr=edudata) for current terms.

## What input does the Actor accept?

The required field is `profileUrls`, an array containing public LinkedIn
profile URLs in the form `https://www.linkedin.com/in/<public-identifier>/`.
Company pages, job URLs and other URL types are not profile inputs.

## What data can a public profile return?

Depending on what LinkedIn exposes, a successful item can include name,
headline, location, follower and connection counts, About, experience,
education, skills, certifications, languages and a profile image. Missing
fields are `null` or empty lists; they are not guessed.

## What does `invalid_url` mean?

The submitted value is not a supported public profile URL. Correct it to a
LinkedIn `/in/` URL and run it again. The original input remains visible in the
Dataset when the Actor writes the audit item.

## What does `login_required` mean if I do not need to log in?

It describes the availability of one profile page, not the Actor's setup. The
Actor tried the public guest view and LinkedIn indicated that more access was
needed. The Actor does not log in and does not accept credentials, so treat that
profile as unavailable public data.

## How is scraping LinkedIn profiles billed?

The public Actor price is **$0.001 per successfully extracted public profile**,
or **$1 per 1,000 successful profiles**. Invalid, inaccessible, blocked,
rate-limited and parser-error inputs do not create the successful-profile
charge. Apify Dataset storage, transfer or other plan-based costs may still
apply.

## Can I export LinkedIn profile data to CSV?

Yes. Export the Apify Dataset as CSV, JSON or Excel after the run. The
repository also includes [`examples/python/export_linkedin_profiles_csv.py`](../examples/python/export_linkedin_profiles_csv.py)
for flattening saved JSON output locally.
