# Output reference

The default Dataset contains one auditable item for each submitted URL that can
be written during the run.

| Field | Type | Always present | Description |
| --- | --- | :---: | --- |
| `success` | Boolean | Yes | `true` only when a public profile was extracted. |
| `status` | String | Yes | Result classification. |
| `inputUrl` | String | Yes | Original submitted URL. |
| `profileUrl` | String or null | Yes | Normalized public profile URL when available. |
| `publicIdentifier` | String or null | Yes | Identifier from the public `/in/` URL. |
| `scrapedAt` | String | Yes | ISO timestamp for the result. |
| `error` | String or null | Yes | Error explanation for unsuccessful items. |
| `profile` | Object or null | Yes | Public profile fields for a successful result. |
| `dataQuality` | Object or null | Yes | Coverage information for fields exposed by the page. |

## Profile fields

When publicly available, `profile` can contain `fullName`, `headline`,
`location`, `followers`, `followersText`, `connections`, `connectionsText`,
`about`, `profilePictureUrl`, `experience`, `education`, `skills`,
`certifications` and `languages`.

Missing fields remain `null` or an empty list. The Actor does not invent or
infer profile data.

## Data quality

`dataQuality.level` is one of:

| Level | Meaning |
| --- | --- |
| `extended` | Basic identity fields plus one or more additional public sections. |
| `core` | The public page exposed the basic identity fields only. |
| `limited` | Fewer basic fields than usual were available. |

Use `dataQuality.publicFields` and `publicFieldCount` before assuming that a
profile has an About, experience or education section.

## Status values

`success`, `invalid_url`, `not_found`, `login_required`, `blocked`,
`rate_limited`, `network_error` and `parse_error` are possible statuses.

`login_required` is an availability result from LinkedIn's public guest view;
it is not a request for the user to log in or provide credentials.
