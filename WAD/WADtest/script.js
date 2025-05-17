// Wait for the DOM to fully load
$(document).ready(function () {
    // Handle hover event on the #hidden element
    $("#hidden").hover(
        function () {
            // When mouse enters, animate color and scale
            $(this).css({
                "transform": "scale(1.04)",
                "transition": "transform 0.2s ease-in-out"
            });
        },
        function () {
            // When mouse leaves, hide the element smoothly
            $(this).fadeOut(1000); // fade out over 0.5 seconds
        }
    );

    // Button to toggle visibility of the info paragraph
    $("#toggle-info").click(function () {
        $(".info-text").slideToggle(); // toggle with sliding animation
    });

    // Optional: Show alert on page load (for demonstration)
    // alert("Page loaded successfully!");
});
