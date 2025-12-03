const userModel = require("../models/userModel");
const bcrypt = require('bcryptjs');


async function userRegisterController(req,res) {
    try{
        const { name, number, email, password} = req.body;
        
        const user = await userModel.findOne({email});
        if(user){
            throw new Error("Already User Exists!");
        }

        if(!name){
            throw new Error("Please Provide name")
        }
        if(!number){
            throw new Error("Please Provide Number")
        }
        if(!email){
            throw new Error("Please Provide Gmail")
        }
        if(!password){
            throw new Error("Please Provide Password")
        }
        const salt = bcrypt.genSaltSync(10);
        const hashPassword =await bcrypt.hashSync(password,salt);


        if(!hashPassword){
            throw new Error("something is wrong");
        }

        const payload={
            ...req.body,
            role: "GENERAL",
            password: hashPassword
        }

        const userData = new userModel(payload);
        const saveUser = await userData.save()

        res.status(201).json({
            data: saveUser,
            success:true,
            error:false,
            message: "User Registered Successfully!"
        })

    }catch(err){
        res.json({
            message: err.message || err,
            error: true,
            success: false,
        })
    }
}

module.exports = userRegisterController;