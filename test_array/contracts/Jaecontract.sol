pragma solidity >=0.4.21 <0.7.0;

contract Jaecontract {
uint[] index;

function setindex(uint content) public{
index.push(content);
}

function getcontent(uint location) public view returns(uint){

return index[location];

}





}
