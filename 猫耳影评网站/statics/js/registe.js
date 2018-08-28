function check_username1() {
    document.getElementById('check1').innerHTML = '长度应在6~10之间<br>设置后不可更改';
}

function check_tel1() {
    document.getElementById('check2').innerHTML = '请输入中国大陆手机号<br>其他用户不可见';
}

function check_tel2() {
    var x = document.getElementById('id_mobile').value;
    if (x.length !== 11){
        document.getElementById('check2').innerHTML = '格式错误';
    }
    else {
        var okimg = document.createElement('img');
        document.getElementById('check2').innerHTML = '正确';
        var child2 =  document.getElementById('check2');
        child2.appendChild(okimg);
    }
}

function check_passwd1() {
    document.getElementById('check3').innerHTML = '密码为6-14个字符';
}

function check_passwd2() {
    var x = document.getElementById('passwd').value;
    if (x.length<6 || x.length>14){
        document.getElementById('check3').innerHTML = '格式错误';
        return false;
    }
    else {
        var okimg = document.createElement('img');
        document.getElementById('check3').innerHTML = '正确';
        var child2 =  document.getElementById('check3');
        child2.appendChild(okimg);
    }
}

function check_test1() {
    document.getElementById('check4').innerHTML = '请输入手机收到的验证码';
}

// function check_test2() {
//     var x = document.getElementById('test').value;
//     if (x.length !== 4){
//         document.getElementById('check4').innerHTML = '验证码错误';
//         return false;
//     }
//     else {
//         var okimg = document.createElement('img');
//         document.getElementById('check4').innerHTML = '正确';
//         var child2 =  document.getElementById('check4');
//         child2.appendChild(okimg);
//     }
// }