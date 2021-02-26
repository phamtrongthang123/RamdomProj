var credit = document.querySelectorAll("td:nth-child(3)");
var subjects = document.querySelectorAll("td:nth-child(2)");
var grade = document.querySelectorAll("td:nth-child(6)");
var GPA_Credits = 0, Credits = 0;
for (var i = 1; i < credit.length; i++) {
    if (
        subjects[i].innerText.includes("Thể dục") ||
        subjects[i].innerText.includes("Anh văn") ||
        subjects[i].innerText.includes("Giáo dục") || Number(grade[i].innerText) < 5
    ) {
        continue;
    }
    GPA_Credits += Number(credit[i].innerText) * Number(grade[i].innerText);
    Credits += Number(credit[i].innerText);
}

chrome.runtime.sendMessage({
    action: "compute",
    GPA_res: (GPA_Credits / Credits).toFixed(2),
    Credits_res: Credits
});