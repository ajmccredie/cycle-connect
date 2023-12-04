// A function to allow formatting of the information added about the services:

document.addEventListener('DOMContentLoaded', function() {
    let serviceDescriptions = document.getElementsByClassName('service_description');
    Array.from(serviceDescriptions).forEach(function(bulletDescription) {
        bulletDescription.innerHTML = bulletDescription.innerHTML.replace(/\*/g, '<br>');
    });
});