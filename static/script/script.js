// A function to allow formatting of the information added about the services:

document.addEventListener('DOMContentLoaded', function() {
    let serviceDescriptions = document.getElementsByClassName('service_description');
    Array.from(serviceDescriptions).forEach(function(bulletDescription) {
        bulletDescription.innerHTML = bulletDescription.innerHTML.replace(/\*/g, '<br>');
    });
});

// Confirm receipt of trading item in market
function showThankYouMessage() {
    alert('Thank you for adding your item. It will show as pending until admin has the opportunity to check and verify the post. You will see when it has been accepted, because the "pending" label will be removed. Happy cycling!');
    return true;
}


// Script to add image thumbnails in userprofile edit and in social rides add ride and edit
function previewImage(event) {
    let reader = new FileReader();
    reader.onload = function(){
        let output = document.getElementById('image-preview');
        output.src = reader.result;
        output.style.display = 'block';
    };
    reader.readAsDataURL(event.target.files[0]);
}

// Trading thank you submission message
document.addEventListener('DOMContentLoaded', function() {
    let form = document.getElementById('trade-form');
    let modal = document.getElementById('thankYouModal');
    let okBtn = document.getElementById('modalOkBtn');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        modal.style.display = "block";
    });

    okBtn.onclick = function() {
        console.log("OK clicked");
        modal.style.display = "none";
        form.submit(); 
    }
});

// Form validation prevention selection of past dates
document.addEventListener('DOMContentLoaded', () => {
    const dateInput = document.getElementById(window.dateFieldId);
    if (dateInput) {
        dateInput.setAttribute('min', window.currentDate);
    }
});

// Pop-up to confirm ride has been added
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('rideForm').addEventListener('submit', function(e) {
        alert('Thank you for adding your ride');
    });
});