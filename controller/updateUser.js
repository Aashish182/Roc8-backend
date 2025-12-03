
const userModel = require("../models/userModel")

async function updateUser(req,res) {
    try{
        const sessionUser = req.userId
        const { userId, email, name, role } = req.body;
        const payload = {
            ...( email && { email}),
            ...( name && { name}),
            ...( role && { role})
        }

        const updatedUser = await userModel.findByIdAndUpdate(userId, payload, {
            new: true, 
            runValidators: true 
        });

        res.json({
            data: updatedUser,
            message: "User Updated",
            success: true,
            error: false
        })

    } catch(err){
        res.json({
            message: err.message || err,
            error: true,
            success: false,
        })
    }
}

module.exports = updateUser;