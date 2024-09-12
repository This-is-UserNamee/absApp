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
    // monthList.value = value !== null ? value : 'All';
    monthList.value = value !== null ? value : `month${new Date().getMonth() + 1}`;
    localStorage.removeItem('monthNum');
}

for (let i = 1; i <= 12; i++){
    styleSheet.setProperty(`--month${i}-property`, 'none');
}

monthList.addEventListener('change', () => {changeMonth(monthList.value)});
changeMonth(monthList.value);

li('form-submit').addEventListener('click', () => {
    let monthTxt = li('form-month');
    localStorage.setItem('monthNum', `month${monthTxt.value}`);
});
li('add1').addEventListener('click', clickAdd);
li('add2').addEventListener('click', clickAdd);

function changeMonth(month) {
    // localStorage.setItem('monthNum', month);
    let cnt = month == 'All' ? lcs('card').length - 1 : lcs(month).length;
    for (let i = 1; i <= 12; i++) {
        if (month == 'All'){
            styleSheet.setProperty(`--month${i}-property`, 'grid');
        } else {
            styleSheet.setProperty(`--month${i}-property`, `month${i}` == month ? 'grid' : 'none');
        }
    }
    styleSheet.setProperty('--null-dialog-property', cnt == 0 ? 'block' : 'none');
}

function clickAdd(){
    const mn = parseInt(monthList.value.replace(/\D/g, ''), 10);
    li('form-month').value = 1 <= mn && mn <= 12 ? mn : new Date().getMonth() + 1;
}

function clickDelete(){
    localStorage.setItem('monthNum', monthList.value);
}