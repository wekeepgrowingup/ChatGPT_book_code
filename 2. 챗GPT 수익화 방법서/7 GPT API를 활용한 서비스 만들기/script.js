$(document).ready(function () {
    const questionUrl = "https://eof3o05oi5vn8op.m.pipedream.net";
    let questionData;
    let currentQuestionIndex = 0;
    let eCount = 0;
    let iCount = 0;
    let nCount = 0;
    let sCount = 0;
    let tCount = 0;
    let fCount = 0;
    let jCount = 0;
    let pCount = 0;
  
    // Start the test
    $("#start-btn").click(function () {
      $(this).addClass("hidden");
      $("#loading-screen").removeClass("hidden");
      fetchQuestionData();
    });
  
    // Fetch question data from the API
    function fetchQuestionData() {
      fetch(questionUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ test: "event" }),
      })
        .then((response) => response.json())
        .then((data) => {
          questionData = data.question.split("\n");
          $("#loading-screen").addClass("hidden");
          $("#question-container").removeClass("hidden");
          showNextQuestion();
        })
        .catch((error) => {
          console.error("Error fetching question data:", error);
        });
    }
  
    // Show the next question
    function showNextQuestion() {
      if (currentQuestionIndex === questionData.length) {
        showResult();
        return;
      }
      const questionText = questionData[currentQuestionIndex];
      const attribute = questionText.slice(-2, -1);
      $("#question-text").text(questionText);
      $("#yes-btn").off("click").on("click", function () {
        handleResponse(attribute, "yes");
      });
      $("#no-btn").off("click").on("click", function () {
        handleResponse(attribute, "no");
      });
      currentQuestionIndex++;
    }
  
    // Handle the user's response to a question
    function handleResponse(attribute, response) {
      switch (attribute) {
        case "E":
          if (response === "yes") {
            eCount++;
          } else {
            iCount++;
          }
          break;
        case "I":
          if (response === "yes") {
            iCount++;
          } else {
            eCount++;
          }
          break;
        case "N":
          if (response === "yes") {
            nCount++;
          } else {
            sCount++;
          }
          break;
        case "S":
          if (response === "yes") {
            sCount++;
          } else {
            nCount++;
          }
          break;
        case "T":
          if (response === "yes") {
            tCount++;
          } else {
            fCount++;
          }
          break;
        case "F":
          if (response === "yes") {
            fCount++;
          } else {
            tCount++;
          }
          break;
        case "J":
          if (response === "yes") {
            jCount++;
          } else {
            pCount++;
          }
          break;
        case "P":
          if (response === "yes") {
            pCount++;
          } else {
            jCount++;
          }
          break;
      }
      showNextQuestion();
    }
  
    // Show the test result
    function showResult() {
      let mbti = "";
      if (eCount > iCount) {
        mbti += "E";
      } else {
        mbti += "I";
      }
      if (nCount > sCount) {
        mbti += "N";
      } else {
        mbti +=  "S";
  }
  if (tCount > fCount) {
    mbti += "T";
  } else {
    mbti += "F";
  }
  if (jCount > pCount) {
    mbti += "J";
  } else {
    mbti += "P";
  }
  $("#question-container").addClass("hidden");
  $("#result-container").text("당신의 MBTI: " + mbti).removeClass("hidden");
  }
  });
  