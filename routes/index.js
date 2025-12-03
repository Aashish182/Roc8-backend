const express = require('express');
const router = express.Router();

// Controller imports
const userRegisterController = require('../controller/userRegister');
const userLoginController = require('../controller/userLogin');
const userDetailsController = require('../controller/userDetails');
const authToken = require('../middleware/authToken');
const userLogout = require('../controller/userLogout');
const createBlog = require('../controller/createBlog');
const blogDetailsController = require('../controller/blogDetails');
const blogUser = require('../controller/blogUser');
const aboutusDetails = require('../controller/aboutusDetails');
const addJob = require('../controller/addJob');
const deleteJob = require('../controller/deleteJob');
const jobDetailsController = require('../controller/jobDetails');
const allUsers = require('../controller/allUsers');
const updateUser = require('../controller/updateUser');
const allQueries = require('../controller/allQueries');
const viewblogdetail = require('../controller/viewblogdetail');
const updateBlog = require('../controller/updateBlog');
const viewquerydetail = require('../controller/viewquerydetail');
const changePassword = require('../controller/changePassword');
const feedback = require('../controller/feedback');
const feedbackDetails = require('../controller/feedbackDetails');
const feedbackUser = require('../controller/feedbackUser');
const userFeedback = require('../controller/userFeedback');
const salaryPredict = require('../controller/salaryPredict');
const courseDetails = require('../controller/courseDetails');

// Routes
router.post("/Register", userRegisterController);
router.post("/Login", userLoginController);
router.get("/user-details", authToken, userDetailsController);
router.get("/userLogout", userLogout);
router.post("/create-blog", createBlog);
router.get("/blogdetails", blogDetailsController);
router.get("/blog-user", blogUser);
router.post("/aboutusdetail", aboutusDetails);
router.post("/addjob", addJob);
router.post("/deletejob", deleteJob);
router.get("/jobdetails", jobDetailsController);
router.get("/AllUser", allUsers);
router.post("/UpdateUser", updateUser);
router.get("/AllQueries", allQueries);
router.post("/viewblogDetails", viewblogdetail);
router.post("/UpdateBlog", updateBlog);
router.post("/viewquerydetails", viewquerydetail);
router.post("/changepassword", changePassword);
router.post("/Feedback", feedback);
router.get("/FeedbackDetails", feedbackDetails);
router.post("/Feedbackuser", feedbackUser);
router.post("/Userfeedback", userFeedback);
router.post("/salarydetails", salaryPredict); 
router.get("/coursedetails",courseDetails);

module.exports = router;
