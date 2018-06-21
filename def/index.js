// 1

let instance;


function fn(o, arr = []) {

    console.log(instance === arr)  // 每次执行方法的时候默认的对象引用地址不相同

    instance = arr;
    arr.push(o);
    return arr;
}

// m
// console.log(fn(1));
// console.log(fn(1));
// console.log(fn(1));

// 2
//将一个数组转为用逗号分隔的参数序列。
function total(...arr) {
    console.log(arr)
    return arr.reduce((con, num) => con + num, 0)
}

// console.log(total(1, 2, 3, 4))
console.log(total({ name: 'leo', age: 25 }))