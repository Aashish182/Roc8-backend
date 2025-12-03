const mongoose = require('mongoose');
const schema = mongoose.Schema;

const feedbackSchema = new mongoose.Schema({
    feedback: String,
    creator: {
        type: schema.Types.ObjectId,
        ref: 'users',
        required : true
    },
    submittedAt: {
        type: Date,
        default: Date.now,
    },
},{
    timestamps: true
})


const feedbackModel = mongoose.model("feedback",feedbackSchema);


module.exports = feedbackModel;