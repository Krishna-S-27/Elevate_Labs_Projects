var x = 42
function foo(y) {
    let unused = 10
    if (y > 0) {
        if (y < 100) {
            console.log("nested ifs")
        }
    }
}
foo(5)
