const Jaecontract = artifacts.require("Jaecontract");



module.exports = function(callback) {
var instance;
Jaecontract.deployed().then(
function(inst){
instance = inst;
var counter = 10;
for(var i = 0; i<counter; i++){
console.log('start store index:');
instance.setindex(i)

}


}





).catch(function (err){
console.log(err);
})













};
