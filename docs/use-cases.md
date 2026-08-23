# Use cases

The Actor is designed for workflows that start with public LinkedIn profile
URLs. It returns the public fields that each page exposes and keeps failures
auditable instead of turning them into guessed data.

## Recruiting research

Provide a list of candidate profile URLs and inspect `profile.fullName`,
`profile.headline`, `profile.location`, `profile.experience` and
`dataQuality.publicFields`.

```json
{
  "profileUrls": [
    "https://www.linkedin.com/in/public-candidate-one/",
    "https://www.linkedin.com/in/public-candidate-two/"
  ]
}
```

Use the output as research context and apply human review. The Actor does not
provide private contact details and should not be used for discriminatory or
high-impact automated decisions.

## CRM or sales enrichment

Start with public profile URLs already associated with a documented business
workflow. Read `fullName`, `headline`, `location`, `about`, `experience` and
`skills` when available. Keep only the fields needed for the stated purpose.

The Actor does not accept company URLs, email addresses or phone numbers as
substitutes for profile URLs.

## Workforce and market research

Submit a controlled list of public profiles and compare structured fields such
as headline, location, experience and skills. Use `scrapedAt` and
`dataQuality` to distinguish current observations from incomplete public pages.

## Auditable batch processing

The Dataset keeps `inputUrl`, `status`, `error` and `scrapedAt` beside the
successful profile. This lets a workflow retry `blocked`, `rate_limited` or
`network_error` items later without silently losing invalid or unavailable URLs.
