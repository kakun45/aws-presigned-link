require("dotenv").congig();

const api_gateway = process.env.API_GATEWAY;

document.addEventListener("DOMContentLoaded", function () {
  // JavaScript code being executed before the HTML document finishes loading. This results in the getElementsByClassName method returning undefined,
  // and subsequently, the addEventListener method cannot be called on it, wrapping code inside a DOMContentLoaded event
  document
    .getElementsByClassName("button1")[0]
    .addEventListener("click", getEmail);

  function getEmail() {
    let email = prompt(
      "Please enter your email. Only verified emails are allowed:"
    );
    if (email !== null) {
      // user entered email. proceed with sending the request to Lambda
      callLambda1(email);
    }
  }

  let isUnauthorizedAlertShown = false;
  let isErrorAlertShown = false;

  function callLambda1(email) {
    // e.preventDefault();
    console.log("A Download was requested");
    // Make an AJAX request to AWS Lambda function
    let xhr = new XMLHttpRequest();
    xhr.open("POST", api_gateway, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
      if (xhr.readyState == 4 && xhr.status === 200) {
        console.log(xhr.responseText);
        alert("Download request was successful!");
      } else if (xhr.status === 401 && !isUnauthorizedAlertShown) {
        // Unauthorized response
        isUnauthorizedAlertShown = true;
        alert(
          "You are not authorized to access this resource. Check the entered spelling on the email"
        );
      } else if (
        xhr.status !== 401 &&
        xhr.status !== 200 &&
        !isErrorAlertShown
      ) {
        // Other error responses
        // console.log("xhr.status:", xhr.status);
        isErrorAlertShown = true;
        console.log(xhr.responseText);
        alert("An error occurred. Please try again later.");
      }
    };

    let payload = JSON.stringify({ email: email });

    xhr.send(payload);
  }

  // this works, but it's timing is off, shows extra message: Uncaught (in promise) Error: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
  async function callLambda(email) {
    console.log("A Download was requested");

    try {
      const response = await fetch(api_gateway, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email: email }),
      });

      if (response.ok) {
        console.log(await response.json());
        alert("Download request successful!");
      } else if (response.status === 401) {
        alert(
          "You are not authorized to access this resource. Check the spelling of the email"
        );
      }
    } catch (error) {
      console.error(error);
      alert("An Error occures. Pls try again later");
    }
  }
});
