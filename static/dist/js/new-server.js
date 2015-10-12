<script>
    var showFlag={};
    function show(o){
    showFlag[o.name]=o.value;
    if(showFlag.j_type=="M"){
        document.getElementById("a1").style.display="";
    }
    else{
        document.getElementById("a1").style.display="none";
    }};

$('#assetForm').validator({
    timely: 2,
    theme: "yellow_right_effect",
    rules: {
        check_ip: [/^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])(\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])){3}$/, 'ip地址不正确'],
        check_port: [/^\d{1,5}$/, '端口号不正确'],
        type_m: function(element){
                    return  $("#M").is(":checked");
            }
    },
    fields: {
        "j_ip": {
            rule: "required;check_ip",
            tip: "输入IP",
            ok: "",
            msg: {required: "必须填写!"}
        },
        "j_port": {
            rule: "required;check_port",
            tip: "输入端口号",
            ok: "",
            msg: {required: "必须填写!"}
        },
        "j_idc": {
            rule: "required",
            tip: "选择IDC",
            ok: "",
            msg: {checked: "必须填写!"}
        },
        "j_dept": {
            rule: "required",
            tip: "选择部门",
            ok: "",
            msg: {checked: "至少选择一个部门"}
        }
    },
    valid: function(form) {
        form.submit();
    }
});

</script>