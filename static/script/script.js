// Script to add image thumbnails in userprofile and in social rides add ride and edit
function previewImage(event) {
    let reader = new FileReader();
    reader.onload = function(){
        let output = document.getElementById('image-preview');
        output.src = reader.result;
        output.style.display = 'block';
    };
    reader.readAsDataURL(event.target.files[0]);
};

// Button to confirm reporting of posts in forum
document.addEventListener('DOMContentLoaded', function() {
    let reportModal = document.getElementById('reportPostModal');
    let confirmBtn = document.getElementById('confirmReportBtn');
    let cancelBtn = document.getElementById('cancelReportBtn');
    let formToSubmit = null;

    document.querySelectorAll('.report-button').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            reportModal.style.display = "block";
            formToSubmit = this.closest('form');
        });
    });

    confirmBtn.onclick = function() {
        reportModal.style.display = "none";
        if (formToSubmit) {
            formToSubmit.submit();
        };
    };

    cancelBtn.addEventListener('click', function() {
        reportModal.style.display = "none";
    });
});


// Pop-up to confirm user edit actions
document.getElementById('editForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    let form = this;
    let overlay = document.getElementById('popup-overlay');
    let popup = document.getElementById('success-popup');

    overlay.style.display = 'flex';
    popup.style.display = 'block';

    setTimeout(function() {
        setTimeout(function() { 
            overlay.style.display = 'none';
            popup.style.display = 'none';
            form.submit();
        }, 500);
    }, 1500);
});

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
        modal.style.display = "none";
        form.submit(); 
    };
});

// Form validation prevention selection of past dates
document.addEventListener('DOMContentLoaded', () => {
    const dateInput = document.getElementById(window.dateFieldId);
    if (dateInput) {
        dateInput.setAttribute('min', window.currentDate);
    };
});

// Pop-up to confirm cancellation of bookings
document.addEventListener('DOMContentLoaded', function() {
    let cancelModal = document.getElementById('cancelModal');
    let confirmBtn = document.getElementById('confirmCancelBtn');
    let cancelBtn = document.getElementById('cancelModalCloseBtn');
    let formToSubmit = null;

    document.querySelectorAll('.cancel-booking-btn').forEach(btn => {
        btn.addEventListener('click', function(event) {
            event.preventDefault();
            cancelModal.style.display = "block";
            formToSubmit = this.closest('form');
        });
    });

    confirmBtn.onclick = function() {
        cancelModal.style.display = "none";
        if (formToSubmit) {
            formToSubmit.submit();
        };
    };

    cancelBtn.addEventListener('click', function() {
        cancelModal.style.display = "none";
    });
});

// Pop-up to confirm ride has been added
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const modal = document.getElementById('submitRideModal');
    const okBtn = document.getElementById('modalOkBtn');
    const isTrustedOrganiser = document.getElementById('isTrustedOrganiser').value === 'true';

    form.addEventListener('submit', function(event) {
        if (!isTrustedOrganiser) {
            event.preventDefault();
            modal.style.display = "block";
        };
    });

    okBtn.onclick = function() {
        modal.style.display = "none";
        form.submit();
    };
});