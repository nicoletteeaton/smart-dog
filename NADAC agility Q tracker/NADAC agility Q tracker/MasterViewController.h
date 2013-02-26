//
//  MasterViewController.h
//  NADAC agility Q tracker
//
//  Created by Nicolette Eaton on 2/26/13.
//  Copyright (c) 2013 Nicolette Eaton. All rights reserved.
//

#import <UIKit/UIKit.h>

@class DetailViewController;

@interface MasterViewController : UITableViewController

@property (strong, nonatomic) DetailViewController *detailViewController;

@end
