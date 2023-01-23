//
// function getAutoComplete() {
//     var search_query = document.getElementById("search-input").value;
//     var xhr = new XMLHttpRequest();
//     xhr.onreadystatechange = function() {
//         if (xhr.readyState == 4 && xhr.status == 200) {
//             var suggestions = JSON.parse(xhr.responseText);
//             updateDropdown(suggestions);
//         }
//     };
//     xhr.open("GET", "/auto-complete?search-query=" + search_query, true);
//     xhr.send();
// }
//
// function updateDropdown(suggestions) {
//     var select = document.getElementById("cryptocurrency-select");
//     select.innerHTML = "";
//     for (var i = 0; i < suggestions.length; i++) {
//         var suggestion = suggestions[i];
//         var option = document.createElement("option");
//         option.value = suggestion.id;
//         option.innerHTML = suggestion.name + " (" + suggestion.symbol + ")";
//         select.appendChild(option);
//     }
// }
