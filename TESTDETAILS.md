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

### Testing specific to form inputs
| Form field | Blank | Too long/large | Incorrect | Invalid |
| ---- | ----- | ----- | ----- | ----- |

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |

## Marketplace/trading
### Overview
| Test case description | Expected outcome | Pass? |
| ---- | ---- | ---- |

### Testing specific to form inputs
| Form field | Blank | Too long/large | Incorrect | Invalid |
| ---- | ----- | ----- | ----- | ----- |

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |

## Services and Bookings
### Overview
| Test case description | Expected outcome | Pass? |
| ---- | ---- | ---- |

### Testing specific to form inputs
| Form field | Blank | Too long/large | Incorrect | Invalid |
| ---- | ----- | ----- | ----- | ----- |

### Other tests of possible user actions
| Action | Result acceptable? |
| ---- | ---- |

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
