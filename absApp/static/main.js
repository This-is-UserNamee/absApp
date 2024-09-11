function li(id) {
    return document.getElementById(id);
}
function lcs(class_){
    return document.getElementsByClassName(class_);
}

let styleSheet = document.documentElement.style;
let monthList = li('month-list');
{
    let value = localStorage.getItem('monthNum');
    monthList.value = value !== null ? value : 'All';
}

for (let i = 1; i <= 12; i++){
    styleSheet.setProperty(`--month${i}-property`, 'none');
}

monthList.addEventListener('change', () => {changeMonth(monthList.value)});
changeMonth(monthList.value);


function changeMonth(month) {
    localStorage.setItem('monthNum', month);
    let cnt = lcs(month).length;
    for (let i = 1; i <= 12; i++) {
        if (month == 'All'){
            cnt = lcs('card').length;
            styleSheet.setProperty(`--month${i}-property`, 'grid');
        }else{
            styleSheet.setProperty(`--month${i}-property`, `month${i}` == month ? 'grid' : 'none');
        }
    }
    styleSheet.setProperty('--null-dialog-property', cnt == 0 ? 'block' : 'none');
}