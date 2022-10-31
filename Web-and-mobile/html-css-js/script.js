window.addEventListener("load", function ()
{
    // Get click elements.
    let clickButtonElement = document.getElementById("click-button");
    let clickCounterElement = document.getElementById("click-counter");

    // counter value.
    let counter = 0;

    // button click function
    let clickButtonFunction = function () 
    {
        // increment counter
        counter++;

        // update click counter text
        clickCounterElement.innerHTML = counter;
    };

    // attach click function to button.
    clickButtonElement.addEventListener("click", clickButtonFunction);
});