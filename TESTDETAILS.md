This document provides additional testing details for the site. 

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
| Password
(initial sign-up) | States that it is required | Unable to reach this limit in manual testing | If the password does not meet the requirements it says so on the page | Non-matching second password re-renders the page and the user is required to try again |
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

### Buttons
| Button | Performs intended action? | Redirects to the correct place? |
| ---- | ----- | ----- |
|  |  |  |

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |
|  |  |

## Social Rides
### Overview
| Test case description | Expected outcome | Pass? |
| ---- | ---- | ---- |

### Testing specific to form inputs
| Form field | Blank | Too long/large | Incorrect | Invalid |
| ---- | ----- | ----- | ----- | ----- |

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |



## Testing of JavaScript
A limited amount of JavaScript was added to the code
