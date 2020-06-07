const Jaecontract = artifacts.require("Jaecontract");



module.exports = function(callback) {
var instance;
Jaecontract.deployed().then(
function(inst){
instance = inst;
var counter = 5;
for(var i = 0; i<counter; i++){
console.log('get index:');
// i do not know why it does not work.
instance.getcontent(i);


}


}





).catch(function (err){
console.log(err);
})













};
