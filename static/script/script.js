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


// Pop-up to confirm ride has been added
document.addEventListener('DOMContentLoaded', function() {
    let form = document.getElementById('ride-form');
    let modal = document.getElementById('submitRideModal');
    let okBtn = document.getElementById('modalOkBtn');
    let isTrustedOrganiser = document.getElementById('isTrustedOrganiser').value === 'True';

    form.addEventListener('submit', function(event) {
        if (!isTrustedOrganiser) {
            console.log("Form submit event")
            event.preventDefault();
            modal.style.display = "block";
        };
    });

    okBtn.onclick = function() {
        modal.style.display = "none";
        form.submit();
    };
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


// Trading toggle status confirmation
document.addEventListener('DOMContentLoaded', function() {
    let soldModal = document.getElementById('soldConfirmationModal');
    let confirmSoldBtn = document.getElementById('confirmSoldBtn');
    let cancelSoldBtn = document.getElementById('cancelSoldBtn');

    document.querySelectorAll('.btn-toggle-status').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            currentForm = this.closest('form');
            soldModal.style.display = "block";
        });
    });

    confirmSoldBtn.addEventListener('click', function() {
        soldModal.style.display = "none";
        if (currentForm) {
            currentForm.submit();
        }
    });

    cancelSoldBtn.addEventListener('click', function() {
        soldModal.style.display = "none";
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
        form.submit();
        overlay.style.display = 'none';
        popup.style.display = 'none';
    }, 1500);
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
