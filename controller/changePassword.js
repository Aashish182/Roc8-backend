const uploadCampiagnPermission = require("../helper/permission");
const userModel = require("../models/userModel");
const bcrypt = require('bcrypt');


async function changePassword(req,res) {
    const { email, oldPassword, newPassword } = req.body;

    try {
        
        const user = await userModel.findOne({ email });
        if (!user) {
            return res.status(404).json({ success: false, message: 'User not found' });
        }

        const isMatch = await bcrypt.compare(oldPassword, user.password);
        if (!isMatch) {
            return res.status(400).json({ success: false, message: 'Old password is incorrect' });
        }

        const salt = await bcrypt.genSalt(10);
        user.password = await bcrypt.hash(newPassword, salt);

        await user.save();

        res.json({ success: true, message: 'Password changed successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ success: false, message: 'Server error' });
    } 
}
module.exports = changePassword;