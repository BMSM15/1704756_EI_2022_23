// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.9.0;


contract Car_Sales {

    address public minter;
    uint public balanceReceived;
    

    event Sent(address from, address to, uint amount);

    uint public IdPurchase;
    string public BrandCar;
    uint public PriceCar;
    string public ModelCar;
    
    constructor(string memory brandCar, string memory modelCar, uint priceCar , uint idPurchase ) {
        minter = msg.sender;
        BrandCar = brandCar;
        ModelCar = modelCar ;
        PriceCar = priceCar;
        IdPurchase = idPurchase;

    }
    
    function Purchase() public payable {
        require(msg.value >= PriceCar,"Valor incorreto");
        balanceReceived += msg.value;
        emit Sent(msg.sender, minter, msg.value);

    }

    function getBalance() public view returns(uint) {
        return address(this).balance;
    }

    function withdrawMoney() public {
        address payable to = payable(msg.sender);
        to.transfer(getBalance());
    }

}