This document provides additional testing details for the site. Back to [README](/README.md)

# Full details of manual site testing
## Sign-up and profile
### Overview
| Test case description | Expected outcome | Pass? |
| ---- | ---- | ---- |
| User registration | User account is created successfully with a unique username and password | Yes |
| User profile creation | User can create a profile with cycling interests and a biography. | Yes |
| User profile update | User can update their profile information. | Yes |
<br>

### Testing specific to form inputs
| Form field | Blank | Too long/large | Incorrect | Invalid |
| ---- | ----- | ----- | ----- | ----- |
| Username (initial sign-up) | States that it is required | The list of requirements is under the field. If it does not meet the requirements, the page re-renders and the user is required to try again | The list of requirements is under the field. If it does not meet the requirements, the page re-renders and the user is required to try again | Users are told if that username is already taken and asked to select a new one. |
| Password (initial sign-up) | States that it is required | Unable to reach this limit in manual testing | If the password does not meet the requirements it says so on the page | Non-matching second password re-renders the page and the user is required to try again |
| Username (login) | Sign-in button is disabled | - | Sign-in button is disabled and page re-renders | Sign-in button is disabled and page re-renders |
| Password (login) | Sign-in button is disabled | - | Sign-in button is disabled and page re-renders | Sign-in button is disabled and page re-renders |
| Ts and Cs | Page re-renders with form in place | - | Page re-renders with form in place | Page re-renders with form in place |
| Biography (detailed profile) | The field is rendered as blank in the profile view. This is acceptable. | Field stops accepting new characters | Field only accepts text | Field only accepts text |
| Image (detailed profile) | No issue, a default image is provided | The  image cannot be accepted | Users receive a warning by the form field that their file is either not an image, or is corrupt | Users receive a warning by the form field that their file is either not an image, or is corrupt |
| Cycling skills radio buttons (detailed profile) | The field is rendered as blank in the profile view. This is acceptable. | - | - | - |
| Preferred ride type radio buttons (detailed profile) | The field is rendered as blank in the profile view. This is acceptable. | - | - | - |
| Maintenance skills radio buttons (detailed profile) | The field is rendered as blank in the profile view. This is acceptable. | - | - | - |
| Biography (detailed profile - edit) | The field is rendered as blank in the profile view. This is acceptable. | Field stops accepting new characters | Field only accepts text | Field only accepts text |
| Image (detailed profile - edit) | No issue, a default image is provided | The  image cannot be accepted | Users receive a warning by the form field that their file is either not an image, or is corrupt | Users receive a warning by the form field that their file is either not an image, or is corrupt |
| Cycling skills radio buttons (detailed profile - edit) | The field is rendered as blank in the profile view. This is acceptable. | - | - | - |
| Preferred ride type radio buttons (detailed profile - edit) | The field is rendered as blank in the profile view. This is acceptable. | - | - | - |
| Maintenance skills radio buttons (detailed profile - edit) | The field is rendered as blank in the profile view. This is acceptable. | - | - | - |

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |
| Back-up before initial sign-up complete, users are redirected to the sign-in screen | Yes |
| Back-up before Ts and Cs agreed to, page re-renders with Ts and Cs document still displayed. None of the menu items work at this point either | Yes |
| Back-up during detailed profile sign-up redirects to the Welcome page inviting the user to click the button to go to the forum page. | Yes |
| It is possible for the user to fill out a many or as few of the profile details form fields as they wish and then return to edit at another time. | Yes |

## Forum
### Overview
| Test case description | Expected outcome | Pass? |
| ---- | ---- | ---- |
| Post creation | User can create a forum post successfully | Yes |
| Post viewing | User can see the posts created by themselves and others | Yes |
| Post update | User can update their posts | Yes |
| Post deletion | User can delete their own post | Yes |
| Post liking | User can like a post, and the like is recorded correctly | Yes |
| Post liking limit | User can like a post only once, and attempts to like again are prevented | Yes |
| Comment creation | User can add comments to a post | Yes |
| Comment display | Comments are displayed under the respective post | Yes |
| Comment update | User can edit comments they have written | Yes |
| Comment delete | User can delete comments they have written | Yes |
| Forum search | User can obtain search results with posts matching title, content or author. | Yes |

### Testing specific to form inputs
| Form field | Blank | Too long/large | Incorrect | Invalid |
| ---- | ----- | ----- | ----- | ----- |
| Post name | User is told the field cannot be blank | Field stops accepting new characters | Form field only accepts characters, but it is possible to only add spaces as the name | Form field only accepts characters |
| Main forum post | User is told the field cannot be blank | Rich text input only limits the input when the upload size becomes too large.  | Rich text input, users can upload images and links | Trying to upload items not included in text, images or links, returns an error message |
| Search bar | Users are provided with the results of a search for nothing. | Field stops accepting new characters | Form field only accepts characters, but it is possible to only add spaces | Form field only accepts characters |
| Post name (edit)| User is told the field cannot be blank | Field stops accepting new characters | Form field only accepts characters, but it is possible to only add spaces as the name | Form field only accepts characters |
| Main forum post (edit)| User is told the field cannot be blank | Rich text input only limits the input when the upload size becomes too large.  | Rich text input, users can upload images and links | Trying to upload items not included in text, images or links, returns an error message |
| Add comment | Users are told the field cannot be blank | Page re-renders with the form input blank. No error message printed | Only text can be entered. | Form field only accepts characters |
| Edit comment | Users are told the field cannot be blank | Page re-renders with the form input blank. No error message printed | Only text can be entered. | Form field only accepts characters |

### Buttons
| Button | Performs intended action? | Redirects to the correct place? |
| ---- | ---- | ---- |
| Edit forum post | Yes | Yes - Leads to edit form |
| Delete forum post | Yes | Yes - Leads to confirm delete |
| Confirm delete forum post | Yes | Yes - Back to forum without post |
| Report post | Yes | Yes - Leads to confirm report |
| Confirm report post | Yes | Yes - Returns to forum with reported post removed |
| Report post cancel | Yes | Yes - Leads back to forum with post still in place |
| Like post | Yes | Yes - Leads back to forum with the post liked |
| Like post second click | Yes | Yes  - Leads back to the forum with the post ‘unliked’ |
| Edit comment | Yes | Yes - Leads to edit form |
| Delete comment | Yes | Yes - Leads to confirm delete |
| Confirm delete comment | Yes | Yes - Leads back to the comment page with the comment removed |

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |
| Back-up can be pressed at any time during the forms and the previous page is rendered. | Yes |
| Back-up does not restore a reported post to the forum. | Yes |
| Back-up does not delete forum posts, nor does it delete comments. | Yes |

Back to [README](/README.md)

## Marketplace/trading
### Overview
| Test case description | Expected outcome | Pass? |
| ---- | ---- | ---- |
| Item creation | User can create listings for bikes and components with details | Yes |
| Item viewing | User can view bike and component listings | Yes |
| Item edit | User can update the information regarding their listing | Yes |
| Item deletion | User can delete their own listed items | Yes |
| Item status update | User can mark a listed item as no longer available and the status is immediately updated | Yes |
| Admin control and support | Admin can view listings before verifying | Yes |
| Conversation creation | Users can start a conversation with someone selling an item | Yes |
| Conversation view | Both users involved in  the conversation can see the content of the conversation | Yes |

### Testing specific to form inputs
| Form field | Blank | Too long/large | Incorrect | Invalid |
| ---- | ----- | ----- | ----- | ----- |
| Conversation comment | Form input allows this | Summernote field does not limit the number of characters unless the combined size of image and text is too large | Rich text input, users can upload images and links | Trying to upload items not included in text, images or links, returns an error message |
| Title of item | User informed it cannot be blank | Field no longer accepts characters | Misleading titles can be filtered by admin validation | Field only accepts text |
| Description of item (create and edit) | User informed it cannot be blank | User informed it is too large | Misleading descriptions can be filtered by admin validation | Field only accepts text |
| Upload image  (create and edit) | A default image of the logo is provided. | User informed it is too large | Misleading images can be filtered by admin validation | Field only accepts images |
| Category radio buttons  (create and edit) | A default value is given | - | Misleading information can be filtered by admin | - |
| Condition radio buttons  (create and edit) | User told to select a condition | - | Misleading information can be filtered by admin | - |
| Status radio buttons  (create and edit) | A default is given | - | Misleading information can be filtered by admin | - |

### Buttons
| Button | Perform intended action? | Redirects to the correct place? |
| ---- | ---- | ---- |
| Filter (after changing one or both of the drop-down menus) | Yes | Yes - Market with only items containing the search terms | 
| Edit listing | Yes | Yes - Leads to edit form |
| Delete listing | Yes | Yes - Leads to confirm delete |
| Confirm delete listing | Yes | Yes - Confirm delete listing |
| Toggle sold status | Yes | Yes - Leads back to market with item listed as ‘sold’ |
| Start conversation | Yes | Yes - Starts a conversation between the potential buyer and the seller. Returning to the market page the button for that conversation has toggled content from ‘start conversation’ to ‘continue conversation’ |
| Continue conversation | Yes | Yes - Returns to the private conversation between the potential buyer (user) and the seller. |
| Named conversations | Yes | Yes - Leads to the private conversation between the seller and the named potential buyer |

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |
| Back-up does not delete items or conversations | Yes |
| Admin verification required before posts show for other users | Yes |
| Verified posts show for all users | Yes |

The form field being able to be submitted as blank and still start a conversation is a known bug, but removing the summernote field and replacing with a normal text field would remove the ability for the seller to send more pictures easily to the potential buyers if asked.

## Services and Bookings
### Overview
| Test case description | Expected outcome | Pass? |
| ---- | ---- | ---- |
| Service creation | Admin can create a service with details | Yes |
| Service update | Admin can update service information | Yes |
| Service deletion | Admin can delete services | Yes |
| Service booking | Users can make bookings | Yes |
| Booking confirmation | Admin can accept bookings made and change the status from ‘pending’ to ‘confirmed’ | Yes |
| Booking cancellation | Users can cancel their bookings | Yes |

All the form inputs are in the admin part of the site. These form fields are clear regarding what is required, and the fields are validated.

### Buttons
| Button | Performs intended action? | Redirects to the correct place? |
| ---- | ----- | ----- |
| View and book | Yes | Yes - Page listing towns/places with slots |
| Place with slots | Yes | Yes - Details of slots to request bookings (filtered by service and place) |
| Request booking | Yes | Yes - Booking confirmation |
| View bookings | Yes | Yes - Full list of user's bookings |
| Cancel booking | Yes | Yes - Booking cancellation confirmation |
| Confirm cancel booking | Yes | Yes - Bookings list with status returned to ‘cancelled’ |

Additional checks (these all behave as expected):
- Only places with available slots show with the numbers, the others do not render - this is useful because it avoids user confusion.
- User cancels a booking and it is returned to the list as ‘available’
- Users cannot double-book slots.

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |
| Bookings procedures can be backed-up using the browser back-up (until the point a booking is marked as pending) | Yes |
| Back-up does not remove service bookings once they are pending or confirmed | Yes |
| Back-up does not restore cancelled bookings | Yes |

Back to [README](/README.md)

## Social Rides
### Overview
| Test case description | Expected outcome | Pass? |
| ---- | ---- | ---- |
| Proposal creation | User can create a proposal for a group cycling event with details | Yes |
| Proposal viewing | User can view verified proposed group cycling events | Yes |
| Proposal cancellation | Users can cancel proposed group rides | Yes |
| Admin can verify proposed rides | Users who are not already designated as ‘trusted organisers’ can have their rides verified by admin | Yes |
| Badge/number of rides display | The correct number of verified rides displays for the user. | Yes |
| Proposal edit and deletion of un-verified rides | User can edit or delete a ride proposal which has not yet been viewed by other users | Yes |
| Event RSVP | User can sign up to any ride with space | Yes |
| Event attendance | User attendance at event is recorded | Yes |

### Testing specific to form inputs
| Form field | Blank | Too long/large | Incorrect | Invalid |
| ---- | ----- | ----- | ----- | ----- |
| Title of ride | User given message that field cannot be blank | No further text accepted | Poor titles may be changed by admin on verification | Only text accepted in this field |
| Date | Not possible to be completely blank | - | Dates cannot be set in the past, but user can select any future date | Field recognises valid dates and will change invalid inputs |
| Image | Not a mandatory field, so no issue | User warned image is too large | Incorrect images could be uploaded, but found and removed by admin on verification | Only image files accepted. Users receive warnings about invalid file types |
| Route description | User given message that field cannot be blank | User informed of character limit | If a poor assessment is made, admin may be able to see this (if familiar with the route) during verification | Only text accepted |
| Start place | User given message that field cannot be blank | No further text accepted | Checked by admin | Only text accepted |
| End place | User given message that field cannot be blank | No further text accepted | Checked by admin | Only text accepted |
| Start time | Not possible to be completely blank | Input field corrects dates (for example 32 changes to 31 in January, or 30 in April) | Checked by admin. Time cannot be in the past, page will re-render without submitting. | Only valid time inputs accepted |
| Distance | User given message that field cannot be blank | User informed that exceeds limit | If a poor assessment is made, admin may be able to see this (if familiar with the route) during verification | Only numerical input accepted |
| Difficulty | Default value provided | - | If a poor assessment is made, admin may be able to see this (if familiar with the route) during verification | - |
| Attendance register | No update to the attendance of users | - | - | - |

### Buttons
| Button | Performs intended action? | Redirects to the correct place? |
| ---- | ---- | ---- |
| View ride detail | Yes | Yes - Detailed view of ride and those already signed up |
| Sign-up for ride | Yes | Yes - Detailed view with user in list. Sign-up button changes text to ‘cancel registration’ |
| Cancel registration | Yes | Yes - Detailed user view without user in list and button text toggled back to ‘sign-up’ |
| Cancel created ride | Yes | Yes - Ride list with the ride showing as 'cancelled' |
| Edit (non-verified rides only) | Yes | Yes - edit form |
| Delete (non-verified rides only) | Yes | Yes - delete confirmation |
| Delete confirmation | Yes | Yes - rides list without the item that was deleted |

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |
| Back-up from ride creation form returns to rides list with no ride created | Yes |
| Back-up after ride is submitted (modal clicked as 'OK') does not remove proposed ride | Yes |
| Back-up after ride sign-up removes ride sign-up (back-up toggles the button) | Yes |
| Back-up after taking the attendance register returns to the attendance register | Yes |

Back to [README](/README.md)

## Testing of JavaScript
A limited amount of JavaScript was added to the code. The code itself was passed through JSHint with no issues.

| Intended function | Action | Pass? |
| ---- | ---- | ---- |
| Formatting of list items from admin to allow rendering as a list with bullet points in Services and Bookings | Each item from the list had the prefix of '*' removed and was replaced with a line break. This script was made redundant by another solution later. | Yes, but not used in production |
| To add thumbnail images of the new files the user is uploading to improve UX and clarity | Miniature pictures are shown of the new images | Yes |
| Pop-up to confirm whether a user wishes to report a forum post | Pop-up appears with 'confirm' and 'cancel'. 'Confirm' continues to form submission and the report is deleted, 'cancel' returns the user to the forum with no action on the post | Yes |
| Pop-up modal to thank user for submission of trading item | Modal pops up and informs the user that the item will be marked as pending until admin verify it. The form is submitted when the user clicks 'OK' | Yes |
| Additional protection for date input in planning social rides | Date selector has past dates blanked out and unavailable for selection | Yes |
| Pop-up modal to thank user for submission of social ride suggestion | Modal pops up and informs the user that the ride will be marked as pending until admin verify it. The form is submitted when the user clicks 'OK' | Yes |
| Pop-up to confirm whether a user wishes to cancel a booking | Pop-up appears with 'confirm' and 'cancel'. 'Confirm' continues to form submission and the booking is cancelled, 'cancel' returns the user to the bookings list with no action on the booking | Yes |
| Pop-up to confirm successful profile edit | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm successful post edit | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm successful post delete | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm successful post comment edit | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm successful post comment delete | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm successful marketplace listing edit | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm successful marketplace listing delete | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm successful social ride edit | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm successful social ride delete | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm successful social ride cancellation | Pop-up appears to confirm successful action, disappears and the user is directed to the correct next page. | Yes |
| Pop-up to confirm user toggle of status of marketplace item | Pop-up appears to confirm whether the user wishes to proceed in toggling the item status, and tells them what will happen to the post. If the user cancels, it no changes are made. If the user confirms, the post status is changed and the post moves. | Yes |

Back to [README](/README.md)
